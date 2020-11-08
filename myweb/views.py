from django.shortcuts import render
from .affine import encrypt, decrypt, affineForm

# Create your views here.
def index(request):
    return render(request, "frontend/index.html")


def affine(request):
    return render(request, "frontend/affine.html", {"form": affineForm})


def myencrypt(request):
    text = ""
    k0 = 0
    k1 = 0
    myencrypt = ""
    if request.method == "POST":
        k0 = int(request.POST.get("k0"))
        k1 = int(request.POST.get("k1"))
        text = request.POST.get("text")
        myencrypt = encrypt(text, k0, k1)
        return render(
            request,
            "frontend/affine.html",
            {
                "form": affineForm,
                "encrypted": myencrypt,
                "k0": k0,
                "k1": k1,
                "text": text,
            },
        )
    return render(
        request,
        "frontend/affine.html",
        {"form": affineForm, "encrypted": myencrypt, "k0": k0, "k1": k1, "text": text},
    )


def mydecrypt(request):
    text = ""
    k0 = 0
    k1 = 0
    mydecrypt = ""
    if request.method == "POST":
        k0 = int(request.POST.get("k0"))
        k1 = int(request.POST.get("k1"))
        text = request.POST.get("text")
        mydecrypt = decrypt(text, k0, k1)
        return render(
            request,
            "frontend/affine.html",
            {
                "form": affineForm,
                "decrypted": mydecrypt,
                "k0": k0,
                "k1": k1,
                "text": text,
            },
        )
    return render(
        request,
        "frontend/affine.html",
        {"form": affineForm, "decrypted": text, "k0": k0, "k1": k1, "text": text},
    )


def aboutme(request):
    return render(request, "frontend/aboutme.html")
