/**
Problem: Sometimes when I copy-paste some text from PDF's the pasted
result comes with some extra white spaces between words.
removeExtraWhiteSpaces does the tedious job for me and removes 
this extra characters from the current selection.
*/
function removeExtraWhiteSpaces() {
  var selection  = DocumentApp.getActiveDocument().getSelection();
  if(selection) {
    var elements = selection.getRangeElements();
    for (var i = 0; i < elements.length; i++) {
      var element = elements[i];
      if (element.getElement().editAsText) {
        var text = element.getElement().editAsText();
        var textStr = text.getText();
        var textStrArr = textStr.split(/\s+/g);
        text.setText("");
        for (var j = 0; j < textStrArr.length; j++) {
          var word = textStrArr[j];
          var space = (j==textStrArr.length-1) ? "" : " ";
          text.appendText(word + space);
        }
      }
    }
  }
}
