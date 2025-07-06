# Використовуємо офіційний Node.js образ
FROM node:16-alpine AS builder

WORKDIR /app

# Копіюємо залежності
COPY frontend/package.json frontend/yarn.lock ./
RUN yarn install --frozen-lockfile

# Копіюємо фронт-код і будуємо
COPY frontend/. .
RUN yarn build

# Фінальний легковаговий образ для nginx
FROM nginx:stable-alpine

# Копіюємо зібраний билд
COPY --from=builder /app/build /usr/share/nginx/html

# Копіюємо налаштування nginx
COPY Docker/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
