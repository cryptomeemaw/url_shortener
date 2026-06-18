export interface ShortenedUrl {
    code: string
    original_url: string
    short_url: string
}

export async function shortenUrl(url: string): Promise<ShortenedUrl> {
    const response = await fetch('/api/url', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url }),
    })

    if (!response.ok) {
        if (response.status === 422) {
            throw new Error('Please enter a valid URL')
        }
        throw new Error('Something went wrong. Please try again.')
    }

    return response.json()
}