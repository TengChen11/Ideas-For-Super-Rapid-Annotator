import gradio as gr

#with gr.Blocks(title = 'Super Rapid Annotator',  theme=gr.themes.Glass()) as demo:
#with gr.Blocks(title = 'Super Rapid Annotator') as demo:
#    gr.Markdown()

#demo.launch(share = False)

textbox = gr.Textbox(
        show_label=False, placeholder="Enter text and press ENTER", container=False
    )
demo = gr.Blocks(theme='HaleyCH/HaleyCH_Theme')

with demo:
    with gr.Row():
        with gr.Column(scale=10):
            gr.Markdown("""# Super Rapid Annotator demo
                            For more information, take a look to this link: https://github.com/RedHenLab/RapidAnnotator-2.0    
                         """)

    with gr.Row():
        video = gr.Video(label="Input Video")
        with gr.Column(scale=3):
            chatbot = gr.Chatbot(label="Video-LLaVA", bubble_full_width=True)
            with gr.Row():
                with gr.Column(scale=8):
                    textbox.render()
                with gr.Column(scale=1, min_width=50):
                    submit_btn = gr.Button( 
                        value="Send", variant="primary", interactive=False
                    )
            with gr.Row(elem_id="buttons") as button_row:
                upvote_btn = gr.Button(value="👍  Upvote", interactive=False)
                downvote_btn = gr.Button(value="👎  Downvote", interactive=False)
                flag_btn = gr.Button(value="⚠️  Flag", interactive=False)
                stop_btn = gr.Button(value="⏹️  Stop Generation", interactive=False)
                regenerate_btn = gr.Button(value="🔄  Regenerate", interactive=False)
                clear_btn = gr.Button(value="🗑️  Clear history", interactive=False)
        with gr.Column(scale=1):
            with gr.Row():
                gr.JSON(value=None, label="Extracted questions and keywords")
            with gr.Row():
                out = gr.JSON(value=None, label="JSON output")
                btn = gr.Button("download")
            with gr.Row():    
                gr.Dataframe(value=None, label="CSV")
                btn = gr.Button("download")
demo.launch(share=False)