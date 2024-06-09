const CACHE_NAME = 'flask-app-cache-v1';
const urlsToCache = [
    '/',
    '/static/_9b6a6904-b6cd-416b-88b1-ba3d981c9fed.jpeg',
    '/static/_9b6a6904-b6cd-416b-88b1-ba3d981c9fed.ico',
    '/static/manifest.json',
    '/static/style.css'
];

self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => cache.addAll(urlsToCache))
    );
});

self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                return response || fetch(event.request);
            })
    );
});
