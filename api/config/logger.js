const { createLogger, format, transports } = require('winston');

const requestLogger = createLogger({
  level: 'info',
  format: format.combine(
    format.timestamp({ format: 'YYYY-MM-DD HH:mm:ss' }),
    format.printf(({ timestamp, level, message }) => {
      return `[${timestamp}] ${level}: ${message}`;
    })
  ),
  transports: [
    new transports.File({ filename: 'logs/requests.log', level: 'info' }),
  ],
});

const serverLogger = createLogger({
  level: 'info',
  format: format.combine(
    format.timestamp({ format: 'YYYY-MM-DD HH:mm:ss' }),
    format.printf(({ timestamp, level, message }) => {
      return `[${timestamp}] ${level}: ${message}`;
    })
  ),
  transports: [
    new transports.Console(),
    new transports.File({ filename: 'logs/server.log', level: 'info' }),
    new transports.File({ filename: 'logs/error.log', level: 'error' }),
  ],
});

module.exports = { requestLogger, serverLogger };
