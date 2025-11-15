
const API_BASE_URL = "http://localhost:8000";

export async function fetchNotes() {
    const res = await fetch(`${API_BASE_URL}/notes`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${localStorage.getItem("token")}`,
        },
    });

    if (!res.ok) {
        throw new Error('Failed to fetch notes');
    }

    return res.json();
}

export async function createNote(noteData) {
    const res = await fetch(`${API_BASE_URL}/notes`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${localStorage.getItem("token")}`,
        },
        body: JSON.stringify(noteData),
    });
    
    if (!res.ok) {
        throw new Error('Failed to create note');
    }

    return res.json();
}