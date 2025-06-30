// logger.js

const levels = {
  DEBUG: 'debug',
  INFO: 'info',
  WARN: 'warn',
  ERROR: 'error',
};

const isDev = process.env.NODE_ENV !== 'production';

function log(level, message, data = null) {
  if (!isDev && level === levels.DEBUG) return; // skip debug logs in prod

  const logMessage = `[${new Date().toISOString()}] [${level.toUpperCase()}] ${message}`;

  switch (level) {
    case levels.DEBUG:
      console.debug(logMessage, data);
      break;
    case levels.INFO:
      console.info(logMessage, data);
      break;
    case levels.WARN:
      console.warn(logMessage, data);
      break;
    case levels.ERROR:
      console.error(logMessage, data);
      break;
    default:
      console.log(logMessage, data);
  }

  // Optionally send to backend or logging service
  // sendToLoggingService(level, message, data);
}

const logger = {
  debug: (msg, data) => log(levels.DEBUG, msg, data),
  info: (msg, data) => log(levels.INFO, msg, data),
  warn: (msg, data) => log(levels.WARN, msg, data),
  error: (msg, data) => log(levels.ERROR, msg, data),
};

export default logger;
