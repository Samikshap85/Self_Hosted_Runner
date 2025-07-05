FROM node:20-alpine As build
Run apk add --no-cache curl
WORKDIR /app
COPY package*.json ./
Run yarn install
COPY . .
RUN yarn build


FROM nginx:alpine
COPY --from=BUILD /app/dist /var/www/html/
COPY --from=BUILD /app/default.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx" , "-g" , "daemon off;"]