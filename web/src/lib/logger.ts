import log from 'loglevel';

log.setLevel(import.meta.env.MODE === 'production' ? 'warn' : 'debug');

export const logger = {
	debug: (...args: unknown[]) => log.debug('[DEBUG]', ...args),
	info: (...args: unknown[]) => log.info('[INFO]', ...args),
	warn: (...args: unknown[]) => log.warn('[WARN]', ...args),
	error: (...args: unknown[]) => log.error('[ERROR]', ...args)
};
