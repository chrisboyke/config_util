# Hippo HTML Extractor

The Hippo HTML Extractor script extracts HTML of a given site for use in Hippo CMS. Saving
the HTML with your browser doesn't extract any fonts, images referenced in the CSS files.
This script saves all referenced resources in HTML and CSS.

Additionally, it can save the HTML as FTL (Freemarker) and automatically put links to
resources in the <@hst.webfile/> tags. You can simply copy the Freemarker file and the
resource folders to Experience, and you should be good to go.

## Requirements
To run the script you need Python 2.7.9 or higher. [Download Python 2.7.x here](https://www.python.org/downloads/release/python-2713/)

You also need the [lxml library](http://lxml.de/installation.html) and the
[requests library](http://docs.python-requests.org/en/master/user/install/#install). You can install these
via the command line when you have Python >= 2.79 installed:
```bash
    $ pip install lxml
    $ pip install requests
```

## Usage
Run the following command in the folder that contains the `extract.py` script.
```bash
    $ python extract.py URL OUTPUT_FOLDER
```

This downloads the HTML from the specified URL and downloads any resources referenced in
the HTML and CSS. After this, you can copy all the subfolders to your project's webfiles
folder (on Mac/Linux):
* v12: `cp -R OUTPUT_FOLDER PATH_TO_PROJECT/repository-data/webfiles/src/main/resources/site/home-oasis`

Finally, copy and overwrite the base-layout.ftl file in your project:
* v12: `cp OUTPUT_FOLDER/base-layout.ftl PATH_TO_PROJECT/repository-data/webfiles/src/main/resources/site/home-oasis/freemarker (e.g. myhippoproject)`

The site should now look very similar if not exactly like the site that you have extracted.
For demos, you will still need to break down the template in sub templates (header, main,
footer, etc.) and do the same for components.

## Other
Show help with all available options:
```bash
    $ python extract.py -h
```
