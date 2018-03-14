import logging
logger = logging.getLogger('uvcsite.ukh.schulportal')

def log(message, summary='', severity=logging.DEBUG):
    logger.log(severity, '%s %s', summary, message)
