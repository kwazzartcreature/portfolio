FROM node:22-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm install && npm cache clean --force

COPY . .

RUN npm run build


FROM node:22-slim

WORKDIR /app

COPY --from=builder /app/package*.json ./
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/build ./build
COPY --from=builder /app/server/server.js ./server/server.js

# ENV BODY_SIZE_LIMIT=5242880

EXPOSE 3000

CMD ["node", "build"]