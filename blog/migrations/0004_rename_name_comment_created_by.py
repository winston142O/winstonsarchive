# Generated by Django 4.2.7 on 2024-01-30 20:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_remove_post_content_post_body_alter_comment_body"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="name",
            new_name="created_by",
        ),
    ]
