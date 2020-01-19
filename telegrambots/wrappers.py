
# Wrapper to restrict bot functions to admins
def restricted(fn):
    def wrapper(bot, update, *args, **kwargs):
        user_id = update.effective_user.id
        if user_id not in self.config['ADMINS']:
            # TODO: send message that user is not permitted
            print(f'Unauthorized access denied for {user_id}')
            return
        return fn(bot, update, *args, **kwargs)
    return wrapper
