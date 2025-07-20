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
