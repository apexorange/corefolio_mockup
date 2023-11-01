import random
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

    # Extract keywords from local gallery

    @staticmethod
    def get_all_keywords(gallery: list) -> list:
        all_rows_of_keywords = []
        for g in gallery:
            all_rows_of_keywords.append(g['Keywords'])
        all_keywords = [item for sublist in all_rows_of_keywords for item in sublist]\
                       + [""] + [""] + [""] + [""] + [""] + [""] + [""] + [""]
        return all_keywords

    @staticmethod
    def choose_random_groups_of_keywords(all_keywords: list):
        random_keyword_list = []
        num_keywords = random.randint(0, 5)
        for i, e in enumerate(all_keywords):
            random_keyword_selector_seed = random.randint(0, len(all_keywords) - 1)
            if len(random_keyword_list) < num_keywords:
                random_keyword_list.append(all_keywords[random_keyword_selector_seed])
        return list(set(random_keyword_list))

    # Extract categories from local gallery

    @staticmethod
    def get_all_categories(gallery: list) -> list:
        all_rows_of_categories = []
        for g in gallery:
            all_rows_of_categories.append(g['Categories'])
        return list(set(all_rows_of_categories))

    @staticmethod
    def choose_random_groups_of_categories(all_categories: list):
        random_category_list = []
        num_categories = random.randint(0, 1)
        for i, e in enumerate(all_categories):
            random_category_selector_seed = random.randint(0, len(all_categories) - 1)
            if len(random_category_list) < num_categories:
                random_category_list.append(all_categories[random_category_selector_seed])
        return random_category_list

    # Check login status

    @property
    def is_user_logged_in(self):
        if not self.logged_in:
            return False
        else:
            return True

    # Determine active form

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
        print("---------------------")
        print("CURRENT PAGE: Sign-in")
        print("---------------------")

    @staticmethod
    def load_welcome():
        print("---------------------")
        print("CURRENT PAGE: Welcome")
        print("---------------------")

    @staticmethod
    def load_debug_form():
        print("------------------------")
        print("CURRENT PAGE: Debug Form")
        print("------------------------")

    @staticmethod
    def load_main(selected_categories: list, selected_keywords: list):
        if selected_categories or selected_keywords:
            print("--------------------------")
            print("CURRENT PAGE: Main Gallery")
            print("--------------------------")

    def create_report(self):
        print(f'ALL_KEYWORDS: {self.get_all_keywords(self.local_gallery)}')
        print("---------------------")
        # print(f'RANDOM_KEYWORD: {self.choose_random_selected_keywords(self.get_all_keywords(self.local_gallery))}')
        print(f'RANDOM_KEYWORD LIST: {self.choose_random_groups_of_keywords(self.get_all_keywords(self.local_gallery))}')
        print("---------------------")
        print(f'ALL_CATEGORIES: {self.get_all_categories(self.local_gallery)}')
        print("---------------------")
        # print(f'RANDOM_CATEGORY: {self.choose_random_selected_categories(self.get_all_categories(self.local_gallery))}')
        print(f'RANDOM_CATEGORY LIST: {self.choose_random_groups_of_categories(self.get_all_categories(self.local_gallery))}')
        print("---------------------")

    def initialize_and_display(self):
        # self.activate_and_load_keyword_autocomplete(Globals.active_keywords)
        self.detect_active_form()
        self.create_report()


# Create gallery item

class GalleryItem:
    def __init__(self, slide_idx, title, categories, keywords):
        self.slide_idx = slide_idx
        self.title = title
        self.keywords = keywords
        self.categories = [categories]

    def __str__(self):
        return f'{self.slide_idx}\n{self.title}\n{self.categories}\n{self.keywords}\n_______________________________\n'


# Create instance of Base class

base = Base()
base.initialize_and_display()

# Create instance of gallery for Base Class

live_gallery = base.local_gallery

# for g in live_gallery:
#     print(str(GalleryItem(g['Index'], g['Slide_Title'], g['Categories'], g['Keywords'])))

random_keys = base.choose_random_groups_of_keywords(base.get_all_keywords(live_gallery))
random_cats = base.choose_random_groups_of_categories(base.get_all_categories(live_gallery))

print('-------------------------')
print(random_keys)
print(random_cats)

live_filter_lst: list = list(set(random_cats + random_keys))

print(f'Active filters: {live_filter_lst}\n')

for g in live_gallery:
    for live_filter in live_filter_lst:
        if live_filter in g['Keywords']:
            print(g['Index'])
            print(str(GalleryItem(g['Index'], g['Slide_Title'], g['Categories'], g['Keywords'])))