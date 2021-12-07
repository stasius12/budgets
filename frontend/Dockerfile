FROM node:17-alpine as builder

WORKDIR /app

COPY yarn.lock ./
COPY package.json ./

RUN yarn && yarn global add @quasar/cli

COPY . .

RUN quasar build


FROM nginx:alpine as production-build

COPY .nginx/nginx.conf /etc/nginx/nginx.conf

RUN rm -rf /usr/share/nginx/html/*

COPY --from=builder /app/dist/spa /usr/share/nginx/html

EXPOSE 80
ENTRYPOINT ["nginx", "-g", "daemon off;"]
