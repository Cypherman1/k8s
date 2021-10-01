FROM node:alpine

WORKDIR /usr/myapp

COPY package.json .

RUN yarn install --force

COPY . .

CMD ["yarn","start"]