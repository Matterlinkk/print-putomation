<h2>print-putomation</h2>
<h4>1. About project</h4>
This project was created for the template of the newspaper, the essence was to load into the folder files format .jpeg, .jpg, .png tracked their appearance, then take a picture of arbitrary size and compress to the desired size, make it black and white and place it in the right place (A4, on which it is located must be transparent), then the printer automatically print it
<h4>2. Installation Instructions:</h4>
Language version:
<el>
  <li>python - 3.10.2</li>
</el>
Libraries used:
<el>
  <li>pillow - 10.0.0</li>
  <li>win32printing - 0.1.3</li>
</el>
In addiction, the folder with files should contain three folders named as:
<br>"for_print", "photos", "printed_photos"
<h4>3. Examples of use:</h4> 
When using the code, pictures should be placed in <i>photos</i>, after which they will be sent as templates to <i>for_print</i>, and after automated printing sent to some "disposal" - <i>printed_photos</i>
<br>
<a href=https://github.com/Matterlinkk/print-putomation/assets/122081802/4660d7c4-0c36-4d27-a0d7-93e252e19fae>[Example of created template]</a>
<br> After creating such a template, as soon as a file is detected, it goes straight to printing
