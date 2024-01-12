// auth.js
export function getAuthHeader() {
    const token = localStorage.getItem('token');
    return token ? `Bearer ${token}` : '';
}
