# joe: judicious observation emitter

I finetuned a GPT-2 model on a bunch of text messages between me and a couple of
friends, and exposed the model through a simple web interface. As a bonus, I can
write this side project off as a Christmas present.

Consider this code hackathon-quality.

## Architecture

I know very little about machine learning, and continue to be committed to
knowing as little about it as possible.
[minimaxir's](http://github.com/minimaxir) work has thankfully made this
incredibly easy.

Here's the bird's eye view:

* To build a dataset to train the model on, I extracted messages from some
  Signal backups and a Slack export (see [extract/][extract/]). I wrote the
  messages (separated by person) to a text file.

* To train the model, I used
  [minimaxir/gpt-2-imple][https://github.com/minimaxir/gpt-2-simple] running on a
  Google Colab notebook. The process is well-described there.

* I generated a bunch of text on Google Colab (my personal laptop is far too
  delicate for such work), cached it in-repo, and wrote a simple frontend that
  pretends like the text is being generated on the fly. There's no real reason
  to lie, except for effect. Good enough for me.

The original plan was to use the finetuned model with
[minimaxir/gpt-2-cloud-run][https://github.com/minimaxir/gpt-2-cloud-run] but I
didn't like the results with 124M, and Google makes it literally impossible to
deploy anything with a GPU if you have a "new" GCP account.


## Usage

### Running locally

    $ FLASK_ENV=development FLASK_APP=app/main.py flask run

### Deploying to Google Cloud Run

    $ docker build app joe
    $ docker push ghcr.io/<project_name>/joe

Then provision the container with Google Cloud Run. This is very "now draw the
rest of the owl"-esque but I don't have it in me to dig out the exact CLI
commands. It's straightforward-enough in the console (remember to set the port
to 80).

I feel like it's against convention to put a project-level Dockerfile anywhere
besides the top-level, but I have a bunch of stuff in my local copy of this
repo's top-level and moving it seemed like the simplest solution.

## Looking forward

I'm still learning about this GPT-2 business, but reading through the
gpt-2-simple README, I suspect that I may not have delineated documents
correctly; I placed each SMS in a file separated only by newlines. I may have
had to prefix/suffix each of the messages -- might look into this in the future.

