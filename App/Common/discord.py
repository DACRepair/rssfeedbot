from discord_webhook import DiscordEmbed, DiscordWebhook
from App.Models.feed_entries import FeedEntry


class Discord:
    def __init__(self, url: str):
        self._client = DiscordWebhook(url)

    def _create_embed(self, post: FeedEntry) -> DiscordEmbed:
        embed = DiscordEmbed()
        embed.set_title(post.title)
        if len(post.text) > 0:
            if len(post.text) > 2048:
                text = post.text[0:2040] + "..."
            else:
                text = post.text
            embed.set_description(text)
        if post.thumb is not None:
            embed.set_thumbnail(url=post.thumb)
        if post.link is not None:
            embed.set_url(post.post)
        embed.add_embed_field(name="Link to Deal:", value=post.link)
        return embed

    def post_entries(self, entries: [FeedEntry]):
        for entry in entries:
            self._client.add_embed(self._create_embed(entry))
        if len(entries) > 0:
            self._client.execute()
