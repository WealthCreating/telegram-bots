response = {
    'content_type': 'text',
    'message_id': 37,
    'from_user': {
        'id': 522933028,
        'is_bot': False,
        'first_name': 'Carter',
        'username': 'carlfarterson',
        'last_name': 'Carlson',
        'language_code': 'en'
    },
    'date': 1579318056,
    'chat': {
        'type': 'private',
        'last_name': 'Carlson',
        'first_name': 'Carter',
        'username': 'carlfarterson',
        'id': 522933028,
        'title': None,
        'all_members_are_administrators': None,
        'photo': None,
        'description': None,
        'invite_link': None,
        'pinned_message': None,
        'sticker_set_name': None,
        'can_set_sticker_set': None
    },
    'forward_from_chat': None,
    'forward_from_message_id': None,
    'forward_from': None,
    'forward_date': None,
    'reply_to_message': None,
    'edit_date': None,
    'media_group_id': None,
    'author_signature': None,
    'text': 'd@d',
    'entities': None,
    'caption_entities': None,
    'audio': None,
    'document': None,
    'photo': None,
    'sticker': None,
    'video': None,
    'video_note': None,
    'voice': None,
    'caption': None,
    'contact': None,
    'location': None,
    'venue': None,
    'animation': None,
    'new_chat_member': None,
    'new_chat_members': None,
    'left_chat_member': None,
    'new_chat_title': None,
    'new_chat_photo': None,
    'delete_chat_photo': None,
    'group_chat_created': None,
    'supergroup_chat_created': None,
    'channel_chat_created': None,
    'migrate_to_chat_id': None,
    'migrate_from_chat_id': None,
    'pinned_message': None,
    'invoice': None,
    'successful_payment': None,
    'connected_website': None,
    'json': {
        'message_id': 37,
        'from': {
            'id': 522933028,
            'is_bot': False,
            'first_name': 'Carter',
            'last_name': 'Carlson',
            'username': 'carlfarterson',
            'language_code': 'en'
        },
        'chat': {
            'id': 522933028,
            'first_name': 'Carter',
            'last_name': 'Carlson',
            'username': 'carlfarterson',
            'type': 'private'
        },
        'date': 1579318056,
        'text': 'd@d'
    }
}

response2 = {
    'content_type': 'text',
    'message_id': 39,
    'from_user': {
        'id': 522933028,
        'is_bot': False,
        'first_name': 'Carter',
        'username': 'carlfarterson',
        'last_name': 'Carlson',
        'language_code': 'en'
    },
    'date': 1579319076,
    'chat': {
        'type': 'private',
        'last_name': 'Carlson',
        'first_name': 'Carter',
        'username': 'carlfarterson',
        'id': 522933028,
        'title': None,
        'all_members_are_administrators': None,
        'photo': None,
        'description': None,
        'invite_link': None,
        'pinned_message': None,
        'sticker_set_name': None,
        'can_set_sticker_set': None
    },
    'forward_from_chat': None,
    'forward_from_message_id': None,
    'forward_from': None,
    'forward_date': None,
    'reply_to_message': None,
    'edit_date': None,
    'media_group_id': None,
    'author_signature': None,
    'text': 'email2@notreal',
    'entities': None,
    'caption_entities': None,
    'audio': None,
    'document': None,
    'photo': None,
    'sticker': None,
    'video': None,
    'video_note': None,
    'voice': None,
    'caption': None,
    'contact': None,
    'location': None,
    'venue': None,
    'animation': None,
    'new_chat_member': None,
    'new_chat_members': None,
    'left_chat_member': None,
    'new_chat_title': None,
    'new_chat_photo': None,
    'delete_chat_photo': None,
    'group_chat_created': None,
    'supergroup_chat_created': None,
    'channel_chat_created': None,
    'migrate_to_chat_id': None,
    'migrate_from_chat_id': None,
    'pinned_message': None,
    'invoice': None,
    'successful_payment': None,
    'connected_website': None,
    'json': {
        'message_id': 39,
        'from': {
            'id': 522933028,
            'is_bot': False,
            'first_name': 'Carter',
            'last_name': 'Carlson',
            'username': 'carlfarterson',
            'language_code': 'en'
        },
        'chat': {
            'id': 522933028,
            'first_name': 'Carter',
            'last_name': 'Carlson',
            'username': 'carlfarterson',
            'type': 'private'
        },
        'date': 1579319076,
        'text': 'email2@notreal'
    }
}

response.keys()

print(response['message_id'])
print(response['from_user'])
print(response['date'])
print(response['chat'])

user = response['from_user']
first_name = user['first_name']
last_name = user['last_name']
username = user['username']


response2
