from .models import Post, FeaturePost, Category
import random

get_all_post = Post.objects.all()
get_all_feature_post = FeaturePost.objects.all()



def custom_context(request):
    recent_post = get_all_post.order_by('-pub_date')[0:10]
    feature_post = get_all_feature_post.order_by('-pub_date')[0]
    random_post = get_all_post[0:3]
    popular_post = get_all_post[5:8]
    suggestion_post = get_all_post[3:6]
    get_all_category = Category.objects.all()

    return {
        'recent_posts': recent_post,
        'posts': get_all_post,
        'feature_post': feature_post,
        'random_posts': random_post,
        'popular_posts': popular_post,
        'suggestion_posts': suggestion_post,
        'categories': get_all_category,
        'hero_post_lists': get_all_post[0:4],
        'hot_post': get_all_post.order_by('-pub_date')[1]
    }


