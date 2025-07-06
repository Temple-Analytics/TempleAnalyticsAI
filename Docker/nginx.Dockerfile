# Образ nginx
FROM nginx:stable-alpine

# Копіюємо власний конфіг для правильного проксі API
COPY Docker/nginx.conf /etc/nginx/conf.d/default.conf

# Робоча папка фронту
COPY frontend/build /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
