FROM node:20-alpine As build
Run apk add --no-cache curl
WORKDIR /app
COPY package*.json ./
Run yarn install

COPY . .

Expose 3000

CMD ["yarn", "start"]