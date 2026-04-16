from django.core.management.base import BaseCommand
from django.utils.text import slugify
from skills.models import Skill, SkillLevel
from core.models import SiteSetting, Feature


class Command(BaseCommand):
    help = 'Load initial CAMDEEP data (7 core skills, settings)'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Loading CAMDEEP initial data...'))

        # 7 Core Skills Data
        skills_data = [
            {
                'name': 'creativity',
                'display_name': 'Creativity',
                'short_description': 'Innovation and original thinking',
                'description': 'Develop creative thinking, innovation, and the ability to generate novel ideas and solutions.',
                'icon': '🎨',
                'order': 1,
            },
            {
                'name': 'analytical',
                'display_name': 'Analytical Thinking',
                'short_description': 'Critical problem analysis',
                'description': 'Master critical thinking, data analysis, and logical reasoning to solve complex problems.',
                'icon': '🧠',
                'order': 2,
            },
            {
                'name': 'management',
                'display_name': 'Management Skills',
                'short_description': 'Organization and leadership',
                'description': 'Learn organization, time management, leadership, and decision-making abilities.',
                'icon': '📊',
                'order': 3,
            },
            {
                'name': 'digital',
                'display_name': 'Digital Skills',
                'short_description': 'Technology proficiency',
                'description': 'Gain proficiency in digital tools, coding, and technology-driven solutions.',
                'icon': '💻',
                'order': 4,
            },
            {
                'name': 'entrepreneurship',
                'display_name': 'Entrepreneurship',
                'short_description': 'Business and venture creation',
                'description': 'Develop entrepreneurial mindset, business planning, and startup skills.',
                'icon': '🚀',
                'order': 5,
            },
            {
                'name': 'ethics',
                'display_name': 'Ethics',
                'short_description': 'Moral responsibility and integrity',
                'description': 'Build ethical decision-making, social responsibility, and moral leadership.',
                'icon': '⚖️',
                'order': 6,
            },
            {
                'name': 'problem_solving',
                'display_name': 'Problem Solving',
                'short_description': 'Solution development',
                'description': 'Master systematic problem-solving, innovation, and creative solution development.',
                'icon': '🔧',
                'order': 7,
            },
        ]

        # Create Skills
        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults={
                    'slug': slugify(skill_data['name']),
                    'short_description': skill_data['short_description'],
                    'description': skill_data['description'],
                    'icon': skill_data['icon'],
                    'order': skill_data['order'],
                    'is_active': True,
                }
            )

            if created:
                self.stdout.write(f"✓ Created skill: {skill_data['display_name']}")
            else:
                self.stdout.write(f"○ Skill already exists: {skill_data['display_name']}")

            # Create Skill Levels
            levels = [
                {
                    'level': 'beginner',
                    'description': f'Just starting to learn {skill_data["display_name"]}',
                    'min_score': 0,
                    'max_score': 25,
                },
                {
                    'level': 'intermediate',
                    'description': f'Developing competency in {skill_data["display_name"]}',
                    'min_score': 26,
                    'max_score': 50,
                },
                {
                    'level': 'advanced',
                    'description': f'Advanced proficiency in {skill_data["display_name"]}',
                    'min_score': 51,
                    'max_score': 75,
                },
                {
                    'level': 'expert',
                    'description': f'Expert level in {skill_data["display_name"]}',
                    'min_score': 76,
                    'max_score': 100,
                },
            ]

            for level_data in levels:
                SkillLevel.objects.get_or_create(
                    skill=skill,
                    level=level_data['level'],
                    defaults={
                        'description': level_data['description'],
                        'min_score': level_data['min_score'],
                        'max_score': level_data['max_score'],
                    }
                )

        # Create Site Settings
        site_settings, created = SiteSetting.objects.get_or_create(
            site_name='CAMDEEP',
            defaults={
                'tagline': 'A Real-World Educational Framework with Global Competencies',
                'description': 'CAMDEEP is an innovative educational initiative designed to equip students with essential 21st-century life skills.',
                'email': 'info@camdeep.edu',
                'phone_primary': '+92 316 8494258',
                'phone_secondary': '+92 305 6256623',
                'street_address': 'Purana Kahna, Near Superior College',
                'city': 'Lahore',
                'state': 'Punjab',
                'postal_code': '54600',
                'country': 'Pakistan',
                'primary_color': '#2563EB',
                'secondary_color': '#FFFFFF',
                'accent_color': '#D4AF37',
            }
        )

        if created:
            self.stdout.write("✓ Created site settings")
        else:
            self.stdout.write("○ Site settings already exist")

        # Create Features
        features_data = [
            {
                'title': 'Project-Based Learning',
                'description': 'Students learn through real-world projects that develop practical skills.',
                'icon': '📚',
                'order': 1,
            },
            {
                'title': 'Trainer Support',
                'description': 'Experienced trainers visit schools twice monthly to guide implementation.',
                'icon': '👨‍🏫',
                'order': 2,
            },
            {
                'title': 'Skill Certification',
                'description': 'Students receive certificates upon completing skill competency requirements.',
                'icon': '🏆',
                'order': 3,
            },
        ]

        for feature_data in features_data:
            Feature.objects.get_or_create(
                title=feature_data['title'],
                defaults={
                    'description': feature_data['description'],
                    'icon': feature_data['icon'],
                    'order': feature_data['order'],
                    'is_active': True,
                }
            )

        self.stdout.write(self.style.SUCCESS('\n✅ Initial data loaded successfully!'))
        self.stdout.write(self.style.WARNING('\n📝 Next steps:'))
        self.stdout.write('   1. Create a superuser: python manage.py createsuperuser')
        self.stdout.write('   2. Run dev server: python manage.py runserver')
        self.stdout.write('   3. Visit admin: http://localhost:8000/admin/')

