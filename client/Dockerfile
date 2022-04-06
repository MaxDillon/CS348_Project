FROM node:14.19-slim

WORKDIR /user/src/app

COPY ./package.json ./

# COPY ./package-lock.json ./


RUN npm install

COPY ./src ./src
COPY ./public ./public

EXPOSE 3000

CMD [ "npm", "start" ]
