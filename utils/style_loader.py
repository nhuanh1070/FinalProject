import os
from Custom_Widgets import loadJsonStyle

def loadStyleJson(self):
    """Hàm này sẽ load file style.json từ thư mục gốc của dự án"""
    # 🟢 Xác định thư mục gốc của dự án (FinalProject)
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    json_path = os.path.join(project_root, "json", "style.json")

    print(f"📂 Đang load JSON từ: {json_path}")  # Debug

    try:
        # 🔥 Load JSON style
        loadJsonStyle(self, self.ui, jsonFiles={json_path})
        print("✅ Style JSON đã được load thành công!")
    except Exception as e:
        print(f"❌ Lỗi khi tải JSON Style: {e}")