def get_display_image(article: dict, watermark: str) -> str:
    if 'image' in article and article['displayImage']:
        return apply_watermark(article['image'], watermark)if watermark else article['image']
    return None

def apply_watermark(image: str, watermark: str) -> str:
    return f"{image} with {watermark}"
