# Use the official Node.js image
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json into the container
COPY package*.json ./

# Install the dependencies
RUN npm install

# Copy the frontend code into the container
COPY . .

# Expose the frontend port
EXPOSE 3000

# Command to run the frontend
CMD ["npm", "start"]
