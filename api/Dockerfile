FROM golang:1.23-alpine AS builder

RUN apk add --no-cache git

WORKDIR /app

COPY go.mod go.sum ./
RUN go mod download

COPY . .
RUN go build -o /build/main ./cmd/server

FROM alpine

RUN apk add postfix && apk add --no-cache busybox-extras && \
    ln -sf /usr/sbin/sendmail /usr/bin/sendmail
RUN postfix start

WORKDIR /root/

COPY --from=builder /build/main ./main
COPY --from=builder /app/config /root/config

COPY ./config/db/pb_migrations /root/pb_migrations

EXPOSE 8080

CMD ["./main", "serve", "--http=0.0.0.0:8080"]