import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

interface WeatherData {
  city: string
  temperature: number
  description: string
}

function App() {
  const [city, setCity] = useState('')
  const [weather, setWeather] = useState<WeatherData | null>(null)
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  // История городов из localStorage
  const [history, setHistory] = useState<string[]>(() => {
    const saved = localStorage.getItem('cityHistory')
    return saved ? JSON.parse(saved) : []
  })

  async function fetchWeather() {
    setError('')
    setWeather(null)
    setLoading(true)

    if (!city.trim()) {
      setError('Введите название города')
      setLoading(false)
      return
    }

    try {
      const response = await fetch(`http://127.0.0.1:8000/weather/fetch/${city}`)
      if (!response.ok) {
        throw new Error('Город не найден или ошибка API')
      }
      const data = await response.json()
      setWeather(data.data)

      // Добавляем город в историю (макс 5, без дубликатов)
      setHistory(prev => {
        const newHistory = [city, ...prev.filter(c => c.toLowerCase() !== city.toLowerCase())].slice(0, 5)
        localStorage.setItem('cityHistory', JSON.stringify(newHistory))
        return newHistory
      })
    } catch (err: any) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank" rel="noreferrer">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank" rel="noreferrer">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>

      <h1>Прогноз погоды</h1>

      <div className="card">
        <input
          type="text"
          placeholder="Введите город"
          value={city}
          onChange={e => setCity(e.target.value)}
          onKeyDown={e => e.key === 'Enter' && fetchWeather()}
        />

        {/* Список истории городов */}
        {history.length > 0 && (
          <ul style={{ cursor: 'pointer', listStyle: 'none', paddingLeft: 0, marginTop: 4, marginBottom: 8 }}>
            {history.map(item => (
              <li
                key={item}
                onClick={() => setCity(item)}
                style={{ padding: '4px 8px', borderBottom: '1px solid #ccc', userSelect: 'none' }}
              >
                {item}
              </li>
            ))}
          </ul>
        )}

        <button onClick={fetchWeather} disabled={loading}>
          {loading ? 'Загрузка...' : 'Получить погоду'}
        </button>

        {error && <p style={{ color: 'red' }}>{error}</p>}

        {weather && (
          <div className="weather-card">
            <h2>{weather.city}</h2>
            <p>Температура: {weather.temperature}°C</p>
            <p>Описание: {weather.description}</p>
          </div>
        )}
      </div>

      <p className="read-the-docs">
        Нажмите на логотипы Vite и React, чтобы узнать больше
      </p>
    </>
  )
}

export default App
