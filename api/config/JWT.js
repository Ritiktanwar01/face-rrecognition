const jwt = require('jsonwebtoken');
const env = require("dotenv")

env.config()

const ACCESS_SECRET = process.env.ACCESS_SECRET;   
const REFRESH_SECRET = process.env.REFRESH_SECRET;

// Generate Access Token (short-lived)
function generateAccessToken(user) {
  return jwt.sign({ id: user._id, email: user.email }, ACCESS_SECRET, { expiresIn: '15m' });
}

// Generate Refresh Token (long-lived)
function generateRefreshToken(user) {
  return jwt.sign({ id: user._id, email: user.email }, REFRESH_SECRET, { expiresIn: '30d' });
}

// Verify Access Token
function verifyAccessToken(token) {
  try {
    return jwt.verify(token, ACCESS_SECRET);
  } catch (err) {
    return null;
  }
}

module.exports = { generateAccessToken, generateRefreshToken, verifyAccessToken };
