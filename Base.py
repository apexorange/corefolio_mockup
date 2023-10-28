import Importer
import Globals


class Base:
    def __init__(self):
        # Import source
        self.local_gallery = Importer.create_local_gallery()

        # Default parameters
        self.return_results = 999
        self.image_width = 200

        # Init lists
        self.all_categories = []
        self.active_keywords = []
        self.selected_categories = []
        self.selected_keywords = []

        # Temporary Status Flags
        self.logged_in = True
        self.show_debug_form_checked = False

    @staticmethod
    def get_all_keywords(gallery: list):
        all_rows_of_keywords = []
        for g in gallery:
            all_rows_of_keywords.append(g['Keywords'])
        all_keywords = [item for sublist in all_rows_of_keywords for item in sublist]
        return all_keywords

    @staticmethod
    def get_all_categories(gallery: list):
        all_rows_of_categories = []
        for g in gallery:
            all_rows_of_categories.append(g['Categories'])
        return all_rows_of_categories

    @property
    def is_user_logged_in(self):
        if not self.logged_in:
            return False
        else:
            return True

    def detect_active_form(self):
        self.load_welcome()
        if self.is_user_logged_in:
            if self.show_debug_form_checked:
                self.load_debug_form()
            else:
                self.load_main(self.selected_categories, self.selected_keywords)
        else:
            self.load_sign_in_page()

    # Startup Form Options

    @staticmethod
    def load_sign_in_page():
        return print("CURRENT PAGE: Sign-in")

    @staticmethod
    def load_welcome():
        return print("CURRENT PAGE: Welcome")

    @staticmethod
    def load_debug_form():
        return print("CURRENT PAGE: Debug Form")

    @staticmethod
    def load_main(selected_categories: list, selected_keywords: list):
        if selected_categories or selected_keywords:
            print("CURRENT PAGE: Main Gallery")

    # Display active form

    def initialize_and_display(self):
        # self.activate_and_load_keyword_autocomplete(Globals.active_keywords)
        self.detect_active_form()
        print(f'ALL_KEYWORDS: {self.get_all_keywords(self.local_gallery)}')
        print(f'ALL_CATEGORIES: {self.get_all_categories(self.local_gallery)}')

    """"""""""""""""""""""""""""""
    """ GALLERY VIEW """
    """"""""""""""""""""""""""""""

    # def get_images_from_gallery(self, gallery: list):
    #     num_results = 1
    #     for i, g in enumerate(gallery):
    #         row_index = i
    #         current_image = i
    #         slide_title = g["Slide_Title"]
    #         categories = g["Categories"]
    #         keywords = g["Keywords"]
    #         remote_path = g["Remote_Path"]
    #         dropbox_url = g["Dropbox_Link"]
    #
    #     def anvil_assemble_gallery_items(self):
    #         # What actually gets put onto the screen in anvil
    #         link_item = []
    #         flow_panel_1 = []
    #
    #         def add_image(item):
    #             print("Image Component Added")
    #             link_item.append(current_image)
    #             # Link_item.add_component(Image(source=URLMedia(remote_path),  # FORM EVENT
    #             #                               width=self.image_width,
    #             #                               height=round(self.image_width * 9 / 16),
    #             #                               spacing_above="small",
    #             #                               background="theme:Gray 300",
    #             #                               role="card")
    #             #                         )
    #
    #         def add_slide_title(item):
    #             print("Title Component Added")
    #             link_item.append(slide_title)
    #             # Link_item.add_component(Label(text=f'{current_image}. {slide_title}',  # FORM EVENT
    #             #                               align="center",
    #             #                               spacing_below="medium",
    #             #                               spacing_above="None",
    #             #                               width=self.image_width,
    #             #                               foreground="black",
    #             #                               role="subheading")
    #             #                         )
    #
    #         def add_keywords(item):
    #             link_item.append(keywords)
    #             print("Keywords Component Added")
    #             # Link_item.add_component(Label(text=f'{"".join(keywords)}',  # FORM EVENT
    #             #                               font_size=14,
    #             #                               foreground="theme:Gray 600",
    #             #                               width=self.image_width,
    #             #                               background='#efefef',
    #             #                               align='center',
    #             #                               spacing_above="none",
    #             #                               spacing_below="medium")
    #             #
    #         self.flow_panel_1.append(link_item)
    #         print(f'Number of results: {num_results}')
    #     num_results += 1

# Display to Anvil

    # def anvil_display_gallery_items(self):
        # print("Anvil output of gallery items")
        # Link_item = Link(row_spacing="small", col_spacing="small")  # FORM EVENT
        # # Check number of visible results from variable
        # if num_results <= self.return_results:
        #     # add image to Link_item
        #     add_image(Link_item)
        #     # If option is checked, add title to Link_item
        #     if self.is_show_title_checked():
        #         add_slide_title(Link_item)  # FORM EVENT
        #     # If option is checked, add keywords to Link_item
        #     if self.is_show_keywords_checked():
        #         add_keywords(Link_item)  # FORM EVENT
        #
        #     Link_item.tag = [slide_title, categories, keywords, remote_path, current_image, row_index, dropbox_url]
        #     Link_item.set_event_handler('click', self.image_click)  # FORM EVENT
        #     self.set_visibility(self.selected_categories, self.selected_keywords, Link_item)
        #
        #     ''' Add Link_Item to flow panel and display '''
        #
        #     self.flow_panel_1.add_component(Link_item)
        #     self.label_results_number.text = f'Total Dataset: {num_results} Slides'
        #     num_results += 1
        # return None

    """"""""""""""""""""""""""""""
    """ SINGLE IMAGE VIEW """
    """"""""""""""""""""""""""""""

    # def image_view_builder(self):
    #     self.column_panel_1.add_component(Image_View(image_num=self.current_clicked_image + 1,
    #                                                  title=(
    #                                                      self.local_gallery[self.current_clicked_image]["Slide_Title"]),
    #                                                  image=URLMedia(self.local_gallery[self.current_clicked_image][
    #                                                                     "Remote_Path"]),
    #                                                  categories=(self.local_gallery[self.current_clicked_image][
    #                                                      "Categories"]).title(),
    #                                                  keywords=(
    #                                                      self.local_gallery[self.current_clicked_image]["Keywords"]),
    #                                                  dropbox_url=(self.local_gallery[self.current_clicked_image][
    #                                                      "Dropbox_Link"])), full_width_row=True)
    #
    # def image_click(self, **event_args):
    #     """This method is called when the link is clicked"""
    #     self.column_panel_1.clear()  # FORM EVENT
    #     self.initialize_and_display()
    #     self.current_clicked_image = event_args['sender'].tag[5]
    #     self.image_view_builder()
    #
    # def next_image_click(self):
    #     self.column_panel_1.clear()  # FORM EVENT
    #     if self.current_clicked_image < len(self.local_gallery) - 1:
    #         self.current_clicked_image += 1
    #         self.image_view_builder()
    #     else:
    #         self.initialize_and_display()
    #
    # def prev_image_click(self):
    #     self.column_panel_1.clear()  # FORM EVENT
    #     if self.current_clicked_image > 0:
    #         self.current_clicked_image -= 1
    #         self.image_view_builder()
    #     else:
    #         self.initialize_and_display()
    #
    # def refresh_selected_image(self):
    #     self.column_panel_1.clear()  # FORM EVENT
    #     # self.load_keywords_from_gallery(self.local_gallery)
    #     self.image_view_builder()
    #
    # def set_visibility(self, sel_cats, sel_keywords, panel):
    #     panel_cats = panel.tag[1]
    #     panel_keywords = panel.tag[2]
    #
    #     if sel_cats and not sel_keywords:
    #         panel.visible = any(cat in panel_cats for cat in sel_cats)
    #
    #     elif sel_keywords and not sel_cats:
    #         panel.visible = any(word in panel_keywords for word in sel_keywords)
    #
    #     elif sel_cats and sel_keywords:
    #         panel.visible = any(word in panel_keywords for word in sel_keywords) and any(
    #             cat in panel_cats for cat in sel_cats)
    #
    #     else:
    #         panel.visible = False


base_form = Base()
base_form.initialize_and_display()
