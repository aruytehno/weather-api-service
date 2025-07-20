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

  async function fetchWeather() {
    setError('')
    setWeather(null)
    if (!city.trim()) {
      setError('Please enter a city')
      return
    }

    try {
      const response = await fetch(`http://127.0.0.1:8000/weather/fetch/${city}`)
      if (!response.ok) {
        throw new Error('City not found or API error')
      }
      const data = await response.json()
      setWeather(data.data) // согласно твоему бекенду: { message, data, id }
    } catch (err: any) {
      setError(err.message)
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

      <h1>Weather App</h1>

      <div className="card">
        <input
          type="text"
          placeholder="Enter city"
          value={city}
          onChange={e => setCity(e.target.value)}
          onKeyDown={e => e.key === 'Enter' && fetchWeather()}
        />
        <button onClick={fetchWeather}>Get Weather</button>

        {error && <p style={{ color: 'red' }}>{error}</p>}

        {weather && (
          <div style={{ marginTop: 20 }}>
            <h2>{weather.city}</h2>
            <p>Temperature: {weather.temperature}°C</p>
            <p>Description: {weather.description}</p>
          </div>
        )}
      </div>

      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
