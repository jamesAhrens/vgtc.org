PRODUCTION_BUCKET=vgtc.org
STAGING_BUCKET=staging.vgtc.org

PRODUCTION_BRANCH=production
STAGING_BRANCH=master

all: site

site:
	./scripts/check_duplicate_permalinks.py
	jekyll build
	./scripts/fix_file_extensions.sh

production: site
	cd _site && ../scripts/sync_with_s3_boto.py $(PRODUCTION_BRANCH) $(PRODUCTION_BUCKET)

staging: site
	cd _site && ../scripts/sync_with_s3_boto.py $(STAGING_BRANCH) $(STAGING_BUCKET)

################################################################################
# sometimes you might want to clean the entire bucket - but this can
# eat a lot of bandwidth, and the website will be missing content for
# a little while. BEWARE

staging-clean:
	cd _site && ../scripts/sync_with_s3_boto.py CLEAN $(STAGING_BUCKET)

production-clean:
	aws s3 rm s3://$(PRODUCTION_BUCKET)/ --recursive
