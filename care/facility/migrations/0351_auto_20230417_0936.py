# Generated by Django 2.2.11 on 2023-04-17 04:06

from django.db import migrations

def migrate_prescriptions(apps, schema_editor):
    PatientConsultation = apps.get_model('facility', 'PatientConsultation')
    Prescription = apps.get_model('facility', 'Prescription')

    for consultation in PatientConsultation.objects.all():
        for advice in consultation.discharge_advice:
            Prescription.objects.create(
                frequency=advice['dosage'].upper(),
                dosage=advice['dosage_new'],
                medicine=advice['medicine'],
                days=advice['days'],
                notes= advice['notes'],
                route=advice['route'].upper(),
                consultation=consultation,
                is_prn=False,
                prescribed_by=consultation.created_by,
            )
        for advice in consultation.prn_prescription:
            Prescription.objects.create(
                medicine=advice['medicine'],
                dosage=advice['dosage'],
                indicator=advice['indicator'],
                max_dosage=advice['max_dosage'],
                min_hours_between_doses=advice['min_time'],
                route=advice['route'].upper(),
                consultation=consultation,
                is_prn=True,
                prescribed_by=consultation.created_by,
            )


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0350_auto_20230417_0907'),
    ]

    operations = [
        migrations.RunPython(migrate_prescriptions),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='discharge_advice',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='prn_prescription',
        )
    ]