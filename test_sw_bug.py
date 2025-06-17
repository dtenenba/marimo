import marimo
import anywidget

__generated_with = "0.13.15"
app = marimo.App(width="medium")

@app.cell  
def _():
    class TestWidget(anywidget.AnyWidget):
        _esm = """
        function render({ model, el }) {
            el.innerHTML = '<div style="padding: 20px; border: 2px solid #4CAF50; border-radius: 8px;">✅ Test Widget - Service Worker Fix Verification</div>';
        }
        export default { render };
        """
    
    widget = TestWidget()
    widget
    return widget,

if __name__ == "__main__":
    app.run()