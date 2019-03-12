import os
from io import BytesIO
from win32com import client
from pathlib import Path
from django.core.files.uploadedfile import InMemoryUploadedFile


class ExportPptFixedFormat():
    def __init__(self, path):
        self.root_path = path
        self.fixed_format = 17
        self.image_dir = None

    def init_app(self):
        try:
            self.powerpoint = client.Dispatch("PowerPoint.Application")
        except Exception as e:
            print(e)

    def init_temp_path(self):
        self.image_dir = Path(__file__).parent.joinpath("images")
        if not self.image_dir.exists():
            self.image_dir.mkdir(parents=True)

    def get_teacher_id(self, name):
        map_dict = {'岳老师': 8}
        return map_dict.get(name)

    def parse_course(self):
        dir = Path(self.root_path)
        for teacher_dir in dir.iterdir():
            id = self.get_teacher_id(teacher_dir.name)
            if not id:
                print("文件夹%s匹配不到老师信息，请确认是否按照标准填写文件名？" % (teacher_dir.name))
                continue
            courses = list(teacher_dir.glob("**/*.ppt*"))
            self.upload_article(id, courses)
        os.remove(self.image_dir)

    def upload_article(self, teacher, courses):
        for course in courses:
            print(teacher,course)
            obj = Article.objects.create(title=course.name, user=teacher)
            self.upload_content(obj, teacher, course)

    def upload_content(self, article, user, course):
        self.export_as_image(course)
        for image in Path(self.image_dir).iterdir():
            url = self.upload_image(user, image)
            seq = self.match_seq(str(image))
            ArticleContent.objects.create(article=article, user=user, type="image", seq=seq, background=url)

    def upload_image(self, user, path):
        with open(path, 'rb') as f:
            data = f.read()
        fd = BytesIO(data)
        size = len(data)
        file_obj = InMemoryUploadedFile(fd, 'background', 'a.jpg', 'image/jpeg', size, charset='utf-8')
        obj = File.objects.create(user=user, url=file_obj, size=size, type="image")
        return obj.url.name

    def export_as_image(self, path):
        image_dir = os.path.splitext(path)[0]
        ppt = self.powerpoint.Presentations.Open(path)
        ppt.SaveAs(image_dir, self.fixed_format)
        ppt.Close()


    def match_seq(self, image_path):
        import re
        pattern = re.compile("\d+")
        return re.findall(pattern, str(image_path))[-1]

    def main(self):
        self.init_app()
        if not self.powerpoint:
            raise ImportError("not have api support")
        self.init_temp_path()
        self.parse_course()


if __name__ == '__main__':
    path = r"D:\course"
    ExportPptFixedFormat(path).main()
