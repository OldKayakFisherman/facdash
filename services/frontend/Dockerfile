FROM node:lts-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

RUN npm install vite@latest

COPY package.json .
COPY package-lock.json .
COPY . .
RUN npm install
RUN npm run build

CMD ["npm", "run", "dev"]
