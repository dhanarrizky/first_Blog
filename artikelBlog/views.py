#from typing import cast, Any, Dict
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# define the models when u want to use the model in this code file
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm

from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.
#def home(request):
#   return render(request, 'Blog/index.html')

class HomeView(ListView):
    model = Post # get Post from models.py code file 
    template_name = 'Blog/index.html'
    cats = Category.objects.all()
    # ordering = ["-id"] # <-- to sort this list view, to sort by id
    ordering = ['-post_date'] # <-- to sort by date
    # if I use - before the parameter, so I can make sort with the last in first page
    
    #=======================
    # this for add chategory dropdown fall
    def get_context_data(self, *args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context
    # if code def above just in homeview, we're can just in home.
    # but if we're try to copy to other view, we're can see in other page
    
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'Blog/article_detail.html'
    
    
    def get_context_data(self, *args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args,**kwargs)
        
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        
        liked=False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        context["cat_menu"] = cat_menu # for return this value
        context["total_likes"] = total_likes # for return this value
        context["liked"] = liked # for return this value
        return context
    
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'Blog/add_post.html'
    #fields = '__all__' #use __all__ for when we want to use all importing like in admin views import page
    
    #if we just want to use same fields in the post method, we can do it
    # for excemple
    # fields = ('title','body') 
    # so we just need add in the title and body form
    

class PostUpdateView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "Blog/Update_post.html"
    #fields = ['title','title_tag','body']

class PostDeleteView(DeleteView):
    model = Post
    template_name = "Blog/delete_post.html"
    success_url = reverse_lazy('homePage')
    
class AddCategoryView(CreateView):
    model = Category
    template_name = 'Blog/add_category.html'
    fields = '__all__'
    
def CategoryView(request, cats):
    # get category from database (models filter)
    category_posts = Post.objects.filter(category=cats.replace('-',' ')) #<-- this codel will get category from models.py
    return render(request, 'Blog/categories.html', {'cats':cats.title().replace('-',' '), 'category_posts':category_posts}) #for slugyfy, we must to add tetle().replace #--> when we want to chance '-' to space

    
def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'Blog/categories_list.html', {'cat_menu_list':cat_menu_list}) 

def LikeView(request,pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else :
        post.likes.add(request.user)
        liked = True
        
    return HttpResponseRedirect(reverse ('article-detail',args=[str(pk)]))

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'Blog/add_comment.html'
    #fields = '__all__'
    success_url = reverse_lazy('homePage')
    
    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk'] #to get this pk and sand to database useing this premier key
        return super().form_valid(form)