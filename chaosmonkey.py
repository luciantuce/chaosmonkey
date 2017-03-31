import os
import argparse
import boto.ec2

access_key = os.getenv('AWS_ACCESS_KEY_ID')
secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')


def get_ec2_instances(region):
    ec2_conn = boto.ec2.connect_to_region(region, aws_access_key_id=access_key, aws_secret_access_key=secret_key)

    # reservations = ec2_conn.get_all_reservations()
    # for reservation in reservations:
    #     print region + ':', reservation.instances
    #
    # for vol in ec2_conn.get_all_volumes():
    #     print region + ':', vol.id
    instances = []
    insnames = ['moolabeta-admin-env', 'moolabeta-admin-ui-env', 'moolabeta-fix-env', 'moolabeta-platform-env', 'moolabeta-platform-worker-env', 'moolabeta-fix-env', 'moolabeta-auth-env2', 'moolabeta-node-server-two-env']

    for insn in insnames:
        reservations = ec2_conn.get_all_instances(filters={"tag:Name": insn})
        instemp = [i for r in reservations for i in r.instances]
        instances = instances + instemp



    # reservations = ec2_conn.get_all_instances(filters={"tag:Name" : "moolabeta-admin*"})
    # instancesadmin = [i for r in reservations for i in r.instances]
    # reservations = ec2_conn.get_all_instances(filters={"tag:Name" : "moolabeta-fix*"})
    # instancesfix = [i for r in reservations for i in r.instances]
    # reservations = ec2_conn.get_all_instances(filters={"tag:Name" : "moolabeta-fix*"})
    # instancesfix = [i for r in reservations for i in r.instances]
    # instances = instancesadmin + instancesfix

    print instances
    print len(instances)


def main():
    regions = ['us-east-1']
    # parser = argparse.ArgumentParser()
    # parser.add_argument('access_key', help='Access Key');
    # parser.add_argument('secret_key', help='Secret Key');
    # args = parser.parse_args()
    global access_key
    global secret_key
    # access_key = args.access_key
    # secret_key = args.secret_key

    for region in regions: get_ec2_instances(region)


if __name__ == '__main__': main()