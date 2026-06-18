import { useState } from 'react'
import { shortenUrl, type ShortenedUrl } from './api'
import './App.css'
import * as React from "react";

function App() {
    const [url, setUrl] = useState('')
    const [result, setResult] = useState<ShortenedUrl | null>(null)
    const [error, setError] = useState('')
    const [loading, setLoading] = useState(false)
    const [copied, setCopied] = useState(false)

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

    async function handleCopy() {
        if (!result) return
        await navigator.clipboard.writeText(result.short_url)
        setCopied(true)
        setTimeout(() => setCopied(false), 1500)
    }

    return (
        <main className="container">
            <h1>URL Shortener take home assessment</h1>

            <form onSubmit={handleSubmit} className="form">
                <input
                    type="text"
                    value={url}
                    onChange={(e) => setUrl(e.target.value)}
                    placeholder="https://example.com/very/long/link"
                    className="input"
                />
                <button type="submit" disabled={loading} className="button">
                    {loading ? 'Shortening…' : 'Shorten'}
                </button>
            </form>

            {error && <p className="error">{error}</p>}

            {result && (
                <div className="result">
                    <a href={result.short_url} target="_blank" rel="noreferrer">
                        {result.short_url}
                    </a>
                    <button onClick={handleCopy} className="copy">
                        {copied ? 'Copied!' : 'Copy'}
                    </button>
                </div>
            )}
        </main>
    )
}

export default App