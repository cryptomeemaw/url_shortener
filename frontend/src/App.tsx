import { useState } from 'react'
import { shortenUrl, type ShortenedUrl } from './api'
import ShortenForm from './components/ShortenForm'
import ResultCard from './components/ResultCard'
import './App.css'
import * as React from "react";

function App() {
    const [url, setUrl] = useState('')
    const [result, setResult] = useState<ShortenedUrl | null>(null)
    const [error, setError] = useState('')
    const [loading, setLoading] = useState(false)

    async function handleSubmit(e: React.SubmitEvent) {
        e.preventDefault()
        setError('')
        setResult(null)
        setLoading(true)
        try {
            const data = await shortenUrl(url)
            setResult(data)
        } catch (err) {
            setError(err instanceof Error ? err.message : 'Unexpected error')
        } finally {
            setLoading(false)
        }
    }

    return (
        <main className="container">
            <h1>URL Shortener</h1>
            <ShortenForm
                url={url}
                loading={loading}
                onUrlChange={setUrl}
                onSubmit={handleSubmit}
            />
            {error && <p className="error">{error}</p>}
            {result && <ResultCard result={result} />}
        </main>
    )
}

export default App