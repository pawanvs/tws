# Step 1: Build the React app
FROM node:18 AS builder
WORKDIR /app
COPY . .
RUN npm install
RUN npm run build

# Step 2: Serve the build using a lightweight web server
FROM node:18-alpine AS production
WORKDIR /app
RUN npm install -g serve
COPY --from=builder /app/build ./build
EXPOSE 5173
CMD ["serve", "-s", "build", "-l", "5173"]
