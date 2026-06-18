import * as React from "react";

interface ShortenFormProps {
    url: string
    loading: boolean
    onUrlChange: (value: string) => void
    onSubmit: (e: React.SubmitEvent) => void
}

function ShortenForm({ url, loading, onUrlChange, onSubmit }: ShortenFormProps) {
    return (
        <form onSubmit={onSubmit} className="form">
            <input
                type="text"
                value={url}
                onChange={(e) => onUrlChange(e.target.value)}
                placeholder="https://example.com/a/very/very/very/very/long/link"
                className="input"
            />
            <button type="submit" disabled={loading} className="button">
                {loading ? 'Shortening…' : 'Shorten'}
            </button>
        </form>
    )
}

export default ShortenForm