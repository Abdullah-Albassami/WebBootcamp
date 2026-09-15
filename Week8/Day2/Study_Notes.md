# Week 8 Day 2 — Quick Study Notes

## 1) Cookies vs Sessions

### Cookies
- Stored in the **browser**
- Good for small preferences
- User can inspect/change them
- Example uses: theme, language, dismissed banner

```python
theme = request.COOKIES.get("theme", "light")
```

Set one:

```python
response.set_cookie(
    "theme",
    "dark",
    max_age=60 * 60 * 24 * 30,
    samesite="Lax"
)
```

Delete one:

```python
response.delete_cookie("theme")
```

### Sessions
- Real data is stored on the **server**
- Browser usually keeps only the **session ID**
- Good for trusted temporary state
- Example uses: cart, login state, multi-page form

```python
cart = request.session.get("cart", [])
request.session["cart"] = cart
```

Remove one value:

```python
request.session.pop("cart", None)
```

Clear the whole session:

```python
request.session.flush()
```

### Easy way to remember

**Cookie = browser value**  
**Session = server-side state**

---

## 2) Always Read State Safely

Cookies can be missing or edited.

```python
theme = request.COOKIES.get("theme", "light")

if theme not in ["light", "dark"]:
    theme = "light"
```

Sessions can also be empty or expired.

```python
cart = request.session.get("cart", [])
```

Use safe defaults instead of assuming the value exists.

---

## 3) Cookie and Session Lifetime

Cookie for 30 days:

```python
max_age = 60 * 60 * 24 * 30
```

Session for 30 days:

```python
request.session.set_expiry(60 * 60 * 24 * 30)
```

Session ends when browser closes:

```python
request.session.set_expiry(0)
```

---

## 4) Important Cookie Security Options

```python
secure=True
httponly=True
samesite="Lax"
```

- `secure` → send only over HTTPS
- `httponly` → JavaScript cannot read it
- `samesite` → limits cross-site sending

Do **not** store passwords or sensitive trusted data in a normal cookie.

---

# Django Forms

## 5) The Main Form Flow

This is the most important sequence:

```text
User submits form
      ↓
request.POST
      ↓
Form(request.POST)
      ↓
is_valid()
      ↓
cleaned_data
      ↓
process/save
      ↓
redirect
```

### Main rule

**Do not trust raw `request.POST`.**

Validate first:

```python
if form.is_valid():
    data = form.cleaned_data
```

---

## 6) GET vs POST

### GET
Used to **show or request data**.

Examples:
- search
- filters
- page number

```python
form = ContactForm()
```

### POST
Used to **submit or change data**.

Examples:
- contact form
- create/update record
- feedback form

```python
form = ContactForm(request.POST)
```

### Memory shortcut

**GET = asking**  
**POST = changing/submitting**

---

## 7) Fields vs Widgets

### Field
Defines **what data is valid**.

```python
name = forms.CharField(max_length=100)
email = forms.EmailField()
```

### Widget
Defines **how the input appears in HTML**.

```python
message = forms.CharField(
    widget=forms.Textarea
)
```

Other widgets:

```python
forms.PasswordInput
forms.Select
forms.CheckboxInput
```

### Remember

**Field = validation**  
**Widget = appearance**

---

## 8) Basic Django Form

```python
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()

    message = forms.CharField(
        widget=forms.Textarea
    )
```

`forms.Form` is useful when the form is **not directly tied to a model**.

---

## 9) Form Inside a View

```python
def contact(request):

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            return redirect("thank_you")

    else:
        form = ContactForm()

    return render(
        request,
        "feedback/contact.html",
        {"form": form}
    )
```

Important detail:

If the form is invalid, render the **same bound form** again so Django can display the errors.

---

## 10) Custom Validation

Validate one field:

```python
def clean_message(self):
    message = self.cleaned_data["message"]

    if len(message) < 20:
        raise forms.ValidationError(
            "Message is too short."
        )

    return message
```

Validate multiple fields together:

```python
def clean(self):
    cleaned = super().clean()

    # compare fields here

    return cleaned
```

### Difference

- `clean_<field>()` → one field
- `clean()` → multiple fields / relationships

---

## 11) CSRF Protection

Every normal POST form should include:

```html
{% csrf_token %}
```

Example:

```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Send</button>
</form>
```

Important distinction:

**CSRF protects the request.**  
**Django Forms validate the values.**

You need both.

---

## 12) Post / Redirect / Get

After a successful POST:

```python
return redirect("thank_you")
```

Why?

Because directly rendering the success page after POST can cause the browser to submit the form again when the user refreshes.

Flow:

```text
POST
 ↓
validate
 ↓
redirect
 ↓
GET success page
```

---

## 13) ModelForm

Use `ModelForm` when the form directly creates or edits a model.

```python
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "published"]
```

Then:

```python
if form.is_valid():
    form.save()
```

### Difference

- `forms.Form` → general form
- `forms.ModelForm` → tied to a model

---

## 14) Common Bugs to Remember

### 403 after submitting
Usually missing:

```html
{% csrf_token %}
```

### Form stays empty after POST
Wrong:

```python
form = ContactForm()
```

Correct:

```python
form = ContactForm(request.POST)
```

### Errors disappear
Do not redirect when the form is invalid.

Render the same page with the bound form.

### `cleaned_data` error
Do not use it before:

```python
form.is_valid()
```

### Duplicate submission
Redirect after successful POST.

---

# Final Memory Sheet

```text
Cookie        = browser value
Session       = server-side state
request.POST  = raw submitted data
is_valid()    = run validation
cleaned_data  = trusted validated values
Field         = validation rule
Widget        = HTML appearance
GET           = request/show
POST          = submit/change
CSRF token    = protects POST request
ModelForm     = form connected to a model
Redirect      = prevents duplicate POST on refresh
```
