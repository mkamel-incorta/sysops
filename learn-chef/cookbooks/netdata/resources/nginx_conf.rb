# Cookbook Name:: netdata
# Resources:: netdata_nginx_conf
#
# Copyright 2016, Abiquo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

resource_name :netdata_nginx_conf

default_action :create

attribute :conf_file, kind_of: String, default: '/etc/netdata/python.d/nginx.conf'
attribute :owner,     kind_of: String, default: 'netdata'
attribute :group,     kind_of: String, default: 'netdata'
attribute :jobs,      kind_of: Hash,   default: {}

action :create do
  t = template new_resource.conf_file do
    cookbook 'netdata'
    source 'nginx.conf.erb'
    mode 0644
    owner new_resource.owner
    group new_resource.group
    variables({
      :jobs => new_resource.jobs
    })
  end
  new_resource.updated_by_last_action(t.updated_by_last_action?)
end
