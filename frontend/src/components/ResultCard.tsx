import { useState } from 'react'
import type { ShortenedUrl } from '../api'

interface ResultCardProps {
    result: ShortenedUrl
}

function ResultCard({ result }: ResultCardProps) {
    const [copied, setCopied] = useState(false)

    async function handleCopy() {
        await navigator.clipboard.writeText(result.short_url)
        setCopied(true)
        setTimeout(() => setCopied(false), 1500)
    }

    return (
        <div className="result">
            <a href={result.short_url} target="_blank" rel="noreferrer">
                {result.short_url}
            </a>
            <button onClick={handleCopy} className="copy">
                {copied ? 'Copied!' : 'Copy'}
            </button>
        </div>
    )
}

export default ResultCard