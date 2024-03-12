def should_show_image(
    item_index: int, 
    article: dict, 
    show_all_images: bool) -> bool:
    condition1 = item_index in [0, 1, 2]
    condition2 = show_all_images
    condition3 = article.get('imageUrl')
    if condition3:
            return condition1 or condition2
    
    

