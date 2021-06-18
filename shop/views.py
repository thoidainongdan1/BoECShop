from django.shortcuts import render, get_object_or_404, get_list_or_404
from shop.models import Category, Product
from comment.models import Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    page = request.GET.get('page')
    paginator = Paginator(products, 6)
    try:
        products = paginator.page(page)

    except PageNotAnInteger:
        products = paginator.page(1)

    except EmptyPage:
        products = paginator.page(1)

    return render(
        request,
        'shop/product/list.html',
        {
            'category': category,
            'categories': categories,
            'products': products,
        }
    )


def product_search(request):
    categories = Category.objects.all()
    results = None
    key = request.POST['key']
    results = Product.objects.filter(name__icontains=key) |\
    Product.objects.filter(description__icontains=key)
    page = request.GET.get('page')
    paginator = Paginator(results, 6)
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(1)

    return render(
        request,
        'shop/product/list.html',
        {'categories': categories, 'products': results, 'key': key}
    )


def product_detail(request, id, slug):

    product = Product.objects.get(id = id, slug = slug, available=True)
    comments = Comment.objects.filter(product = product)
    # stars = [0,0,0,0,0,0]
    # for comment in comments:
    #     star[comment.star] += 1

    return render(
        request,
        'shop/product/detail.html',
        {'product': product, 'comments': comments}
    )
