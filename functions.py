import json


def load_posts() -> list[dict]:
    with open('posts.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_posts_by_tag(tag: str) -> list[dict]:
    final = []

    for post in load_posts():
        if tag.lower() in post['content'].lower():
            final.append(post)

    return final


def add_post(post: dict) -> dict:
    posts: dict[list] = load_posts()
    posts.append(post)

    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file, indent=len(posts), ensure_ascii=False)

    return post
